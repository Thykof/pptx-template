from pptx_template import render


def main():
    input_path = '../propale-type-jinja2.pptx'
    # input_path = '../propale-type-1.pptx'
    model = {
        "president": {
            "prenom": "Oumaima",
            "nom": "Sahnour",
            "email": "oumaima.sahnour@idesys.org",
            "portable": "0600000000",
            "sexe": "f"
        },
        "entreprise": {
            "nom": "PPID",
            "commentaire": "C'est un entreprise qui vend des drones"
        },
        "junior": {
            "nom": "IdéSYS"
        },
        "suiveur": {
            "prenom": "Nathan",
            "nom": "Seva",
            "email": "nathan.seva@idesys.org",
            "portable": "0695816906"
        },
        "etude": {
            "objectif": "Faire 3 sites"
        },
        'pictures': {
        
        }
    }
    output_path = '../propale-generated.pptx'
    render.render_pptx(input_path, model, output_path)

if __name__ == '__main__':
    main()
