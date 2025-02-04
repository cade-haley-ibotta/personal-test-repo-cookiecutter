
def main(*args, **kwargs):
    project_name = '{{ cookiecutter.project_name }}'
    print(f"Running a hook for {project_name} !")

    hook_generated = "./hook_generated.txt"
    print(f"This will create a file called {hook_generated}")
    f = open(hook_generated, "w")
    f.write("Here's a file, created right from the pre_gen_project.py hook")
    f.close()

main()