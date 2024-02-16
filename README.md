# Microservices

Microservices each with its own function
[YouTube Search Pip Website](https://pypi.org/project/youtube-search/)

## Requirements exports

Export the packages installed ```pip freeze | sed 's/@.*//g' > requirements.txt```

If the above does not work the run ```conda env export --name your_env_name > environment.yml``` after which only copy the packages listed under the pip section into the requirements file.
