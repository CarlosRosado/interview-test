'''
File used to hold dynaconf configurations
Also, utilitary functions to deal with envvars and other configurations 
'''
import os

from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[                              # Paths or globs to any toml|yaml|ini|json|py
        "devops/dynaconf/settings.toml",          # a file for main settings
        "devops/dynaconf/.secrets.toml"           # a file for sensitive data (gitignored)
    ],

    environments=True,                    # Enable layered environments
                                          # (sections on config file for development, production, testing)

    load_dotenv=True,                     # Load envvars from a file named `.env`
                                          # TIP: probably you don't want to load dotenv on production environments
                                          #      pass `load_dotenv={"when": {"env": {"is_in": ["development"]}}}

    envvar_prefix=False,                  # variables exported as `DYNACONF_FOO=bar` becomes `settings.FOO == "bar"`
    env_switcher="ENV_FOR_DYNACONF",      # to switch environments `export ENV_FOR_DYNACONF=production`

    dotenv_path="devops/dynaconf/.env"            # custom path for .env file to be loaded
)


def envvar(name):
    """
    Get envvar from dynaconf settings and if not available, from os.environ

    This method is needed to abstract getting values from:
        - .env file (managed by dynaconf)
        - envvars (defined in Azure Functions app settings)
    """
    value = settings.get(name, os.environ.get(name))
    if not value:
        raise RuntimeError(f"{name} could not be found in dynaconf settings nor as an envvar")
    return value

