#
# Copyright 2018-2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import sys
from glob import glob
from setuptools import setup, find_packages

long_desc = """
            Elyra is a set of AI centric extensions to JupyterLab. It aims to help data scientists,
            machine learning engineers and AI developer’s through the model development life cycle complexities.
            """

here = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(here, 'elyra', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

npm_packages_path = "./dist/*.tgz"
auto_extension_path = "./jupyter-config/jupyter_notebook_config.d/*.json"

setup_args = dict(
    name="elyra",
    version=version_ns['__version__'],
    url="https://github.com/elyra-ai/elyra",
    description="Elyra provides AI Centric extensions to JupyterLab",
    long_description=long_desc,
    author="Elyra Maintainers",
    license="Apache License Version 2.0",
    data_files=[('etc/jupyter/jupyter_notebook_config.d', glob(auto_extension_path))],
    packages=find_packages(),
    install_requires=[
        "jupyter_core>=4.0,<5.0",
        "kfp==0.2.2",
        "urllib3==1.24.2",
        "kfp-notebook>=0.7.0",
        "kfp-server-api==0.1.18.3",
        "minio>=5.0.7",
        'nbdime>=2.0.0',
        'jupyterlab>=2.0.0',
        'jupyterlab-git==0.20.0rc0',
        'nbconvert>=5.6.1',
        'notebook>=6.0.3',
        'traitlets>=4.3.2',
        'jsonschema>=3.2.0',
        'requests>=2.9.1,<3.0',
        'entrypoints>=0.3',
        'rfc3986-validator>=0.1.1',
    ],
    include_package_data=True,
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    entry_points={
        'console_scripts': [
            'jupyter-runtimes = elyra.metadata.runtime:RuntimeMetadataApp.launch_instance',
            'jupyter-code-snippets = elyra.metadata.code_snippet:CodeSnippetMetadataApp.launch_instance',
        ],
        'elyra.pipeline.processors': [
            'kfp = elyra.pipeline.processor_kfp:KfpPipelineProcessor'
        ]
    },
)

if "--dev" not in sys.argv:
    setup_args["data_files"].append(('share/jupyter/lab/extensions', glob(npm_packages_path)))
else:
    sys.argv.remove("--dev")

if __name__ == '__main__':
    setup(**setup_args)
