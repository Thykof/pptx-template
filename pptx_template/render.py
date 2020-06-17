from pptx import Presentation
from pptx_template.core import edit_slide


def render_pptx(input_path, model, output_path, skip_model_not_found=False, clear_tags=False):
    ppt = Presentation(input_path)
    for slide in ppt.slides:
        edit_slide(slide, model, skip_model_not_found, clear_tags)
    ppt.save(output_path)
