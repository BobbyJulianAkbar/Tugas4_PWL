import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_jinja2",
    "pyramid_debugtoolbar",
    "waitress",
    "alembic",
    "pyramid_retry",
    "pyramid_tm",
    "SQLAlchemy",
    "transaction",
    "zope.sqlalchemy",
    "pymysql",
    "pyjwt",
    "pyramid_jwt",
]

tests_require = [
    "WebTest",
    "pytest",
    "pytest-cov",
]

setup(
    name="tugas_4_bo",
    version="0.0",
    description="tugas-4-bo",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web pyramid pylons",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "testing": tests_require,
    },
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = tugas_4_bo:main",
        ],
        "console_scripts": [
            "initialize_tugas_4_bo_db=tugas_4_bo.scripts.initialize_db:main",
        ],
    },
)
