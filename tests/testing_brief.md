### pytest
#### steps to run
##### go to project root folder
```bash
cd project_root_folder
```
##### basic
```bash
pytest
```
##### with verbose
```bash
pytest -v
```
##### with prints
```bash
pytest -s
```
##### with markers
```bash
pytest -m marker_name
```
##### including certain markers only
```bash
pytest -m marker_name 
```
##### combinations
###### NOT
```bash
python -m "not marker_name"
``` 
###### OR
```bash
pytest -m "marker_one or marker_two"
```
###### AND
```bash
pytest -m "marker_one and marker_two"
```

#### Reporting
#### install pytest-html
```bash
pip install pytest-html
```

##### generate html
```bash
pytest --html="report.html"
```

##### generate xml
```bash
pytest --junitxml="reports.xml"
```
##### pytest option to run a single function
```bash
pytest -k function_name_or_class_name
```
##### running with custom command line arguments
```bash
pytest --env qa
```

##### pytest with threads
```bash
pip install pytest-xdist
```
###### command to run with number of threads
```bash
pytest -n(number of threads)
```
###### select number of threads based on your system cup configuration
```bash
pytest -nauto
```