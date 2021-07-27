from setuptools import setup

setup(
    name="Hekate Engine Game",
    options = {
        'build_apps': {
            'include_patterns': [
                'Content/maps/*',
                'Content/models/*/*',
                'Content/*',
                'src/defaultMeshes/*.bam'
            ],
            # TODO: Change to gui_application if the logging is finished
            'console_apps': {
                'Hekate Engine Game': 'main.py',
            },
            'plugins': [
                "pandagl",
                "p3openal_audio",
            ],
            'platforms': [
                'win_amd64',
                'manylinux1_x86_64',
            ]
        }
    },
)