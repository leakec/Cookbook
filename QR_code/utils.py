import shutil
import numpy as np
from typing import Tuple, Any
from pathlib import Path

Color = Tuple[float, float, float, float]


def lerp(from_val: Any, to_val: Any, t: Any) -> Any:
    """
    Linearly interpolate.
    """
    return (1.0 - t) * from_val + t * to_val


def inv_lerp(from_val: Any, to_val: Any, t: Any) -> Any:
    """
    Inverse lerp function.
    """
    return (t - from_val) / (to_val - from_val)


def remap(c1: Color, c2: Color, c3: Color, c4: Color, image: Path, new_image: Path):
    """
    Remap from c1 and c2 to c3 and c4.
    """
    from PIL import Image

    c1 = np.array(c1).reshape((1, 1, 4))
    c2 = np.array(c2).reshape((1, 1, 4))
    c3 = np.array(c3).reshape((1, 1, 4))
    c4 = np.array(c4).reshape((1, 1, 4))

    with Image.open(image) as f:
        pix_vals = np.array(f)
        t = inv_lerp(c1, c2, pix_vals / 255.0)
        new_pix_vals = lerp(c3, c4, t) * 255.0
    new_pix_vals = np.nan_to_num(new_pix_vals, nan=255.0)
    new_pix_vals = np.array(new_pix_vals, dtype=np.uint8)

    im = Image.fromarray(new_pix_vals)
    im.save(new_image)


white = (1.0, 1.0, 1.0, 1.0)
black = (0.0, 0.0, 0.0, 1.0)
purple = (0.5, 0.0, 1.0, 1.0)
purple = (0.235, 0.0, 0.322, 1.0)

image = Path("QR_code.png")
new_image = Path("QR_code_recolor.png")

remap(white, black, purple, black, image, new_image)
