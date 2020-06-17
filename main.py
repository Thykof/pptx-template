from pptx_template import render


def main():
    input_path = 'test/data5/in.pptx'
    model = {
        "greeting": "Hello!",
        "client_name": "M. Melpanque"
    }
    output_path = 'test/data5/out.pptx'
    render.render_pptx(input_path, model, output_path)

if __name__ == '__main__':
    main()
