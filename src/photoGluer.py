import os
from PIL import Image, ImageFile, ImageOps
ImageFile.LOAD_TRUNCATED_IMAGES = True


class PhotoGluer:
    def glue_vertical(self, input_dir: str, output_dir: str, params: dict = {}) -> str:
        """Glue images vertically

        Parameters
        ----------
        input_dir : name of input_dirorary directory with images
        output_dir : name of output directory
        params : dictionary with parameters, optional
            name : name of output image, default 'output.jpg'
            width : width of output image, default 1000
            margin : margin between images, default 0
            margin_color : color of margin, default 'white'

        Returns
        -------
        Path to glued image if success
        or empty string if fail
        """

        default_params = {
            'name': 'output.jpg',
            'width': 1000,
            'margin': 0,
            'margin_color': 'white',
        }
        params = {**default_params, **params}

        # Get list of images
        try:
            images = (Image.open(f'{input_dir}/{name}')
                      for name in os.listdir(input_dir))
        except:
            return False

        # Sort images in alphabetical order
        images = list(sorted(images, key=lambda img: img.filename))

        # Rotate images to correct orientation
        images = list(map(ImageOps.exif_transpose, images))

        # Resize images
        images = list(map(lambda img: self.resize_by_width(
            img, params['width']), images))

        # Create background
        height = sum([image.size[1] for image in images])
        height += params['margin'] * (len(images) - 1)
        background = Image.new(
            'RGB', (params['width'], height), params['margin_color'])

        # Paste images
        y_pos = 0
        for image in images:
            background.paste(image, (0, y_pos))
            y_pos += image.size[1] + params['margin']

        # Save image
        save_path = os.path.join(output_dir, params['name'])
        background.save(save_path)

        return save_path

    def resize_by_width(self, image: Image, new_width: int) -> Image:
        """Proportionally resize the photo for a given width"""

        width, height = image.size
        new_height = int(new_width * height / width)
        return image.resize((new_width, new_height))
