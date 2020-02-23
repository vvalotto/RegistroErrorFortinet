from setuptools import setup, find_packages


setup(
    name="errores_fortinet",
    version="1.0.0",
    description="Servicios Web para registrar los errores 504 presentados en los navegadores",

    author="Victor Valotto",
    author_email="vvalotto@enersa.com.ar",

    packages=find_packages(),
    py_modules=['app'],
    include_package_data=True,
    install_requires=['Flask>=1.1.1',
                      'Flask-Cors>=3.0.8',
                      'pyOpenSSL>=19.1.0'],
)