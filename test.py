import cookiecutter
import cookiecutter.main
# cookiecutter.main.cookiecutter('gh:audreyfeldroy//cookiecutter-pypackage')
cookiecutter.main.cookiecutter(
    'boilerplate',
    no_input=True,
    extra_context={
        "project_name": "programmatic_thing",
        "description": "This was made entirely using python without any special input"
    }
)
