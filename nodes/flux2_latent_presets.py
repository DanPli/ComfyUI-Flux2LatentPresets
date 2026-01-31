import torch

class Flux2EmptyLatentPresets:
    """
    Flux 2 Empty Latent Presets
    """

    DESCRIPTION = (
        "Creates an empty latent using official Flux 2–recommended "
        "resolution presets.\n\n"
        "The available presets are derived directly from the Flux 2 "
        "resolution and detail guidelines published by Black Forest Labs.\n\n"
        "Use this node to quickly select a supported megapixel tier and "
        "aspect ratio without manually entering dimensions.\n\n"
        "All presets are divisible by 8 and generate SD-style latents "
        "at 1/8 resolution, suitable for Flux 2 Dev workflows."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (
                    [
                        # min. draft quality
                        "0.15MP | 1:1 | 400 x 400",
                        
                        # 0.5 MP
                        "0.5MP | 1:1 | 704 x 704",
                        "0.5MP | 16:9 | 960 x 544",
                        "0.5MP | 3:2 | 896 x 600",
                        "0.5MP | 4:3 | 832 x 624",
                        "0.5MP | 5:4 | 800 x 640",
                        "0.5MP | 9:16 | 544 x 960",

                        # 1 MP (Standard)
                        "1MP | 1:1 | 1024 x 1024",
                        "1MP | 16:9 | 1344 x 768",
                        "1MP | 3:2 | 1216 x 832",
                        "1MP | 4:3 | 1152 x 864",
                        "1MP | 5:4 | 1120 x 896",
                        "1MP | 9:16 | 768 x 1344",

                        # 2 MP
                        "2MP | 1:1 | 1440 x 1440",
                        "2MP | 16:9 | 1792 x 1024",
                        "2MP | 3:2 | 1728 x 1152",
                        "2MP | 4:3 | 1664 x 1248",
                        "2MP | 5:4 | 1600 x 1280",
                        "2MP | 9:16 | 1024 x 1792",

                        # 4 MP
                        "4MP | 1:1 | 2048 x 2048",
                        "4MP | 16:9 | 2688 x 1536",
                        "4MP | 3:2 | 2432 x 1624",
                        "4MP | 4:3 | 2304 x 1728",
                        "4MP | 5:4 | 2240 x 1792",
                        "4MP | 9:16 | 1536 x 2688",
                    ],
                    {"default": "1MP | 1:1 | 1024 x 1024"}
                ),
                "invert": ("BOOLEAN", {"default": False}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("latent", "width", "height")
    FUNCTION = "generate"
    CATEGORY = "Flux 2/Latents"

    def generate(self, preset, invert, batch_size):
        size_part = preset.split("|")[-1].strip()
        width, height = map(int, size_part.split("x"))

        if invert:
            width, height = height, width

        latent_w = width // 8
        latent_h = height // 8

        latent = torch.zeros(
            [batch_size, 4, latent_h, latent_w],
            device="cpu"
        )

        return ({"samples": latent}, width, height)


NODE_CLASS_MAPPINGS = {
    "Flux2EmptyLatentPresets": Flux2EmptyLatentPresets
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Flux2EmptyLatentPresets": "Flux 2 Empty Latent Presets"
}
