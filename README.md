## What is ZimFarm?

ZimFarm is an open-source web application to connect farmers directly to
consumers.

It allows consumers to create shopping lists of needed food items and
then, using ZimFarm, consumers can view lists of nearby farmers who are
growing those crops and then purchase those items directly from the
farmers using the ZimFarm payment system and even arrange for delivery
directly to their door!


## How to Install ZimFarm
1. Clone or download and extract the project to your PC.

2. Move into the folder zimfarm
```
cd zimfarm
```

3. Create a virtual environment to work in.
```
python3 -m venv .p3
```

4. Activate the virtual environment
```
source .p3/bin/activate
```

5. Install the requirements from the requirements file
```
pip install -r requirements.txt
```

6. Move into the farm_project folder
```
cd farm_project
```

7. Apply the migrations
```
python manage.py migrate
```

8. Start the server
```
python manage.py runserver
```

9. Open your browser at the address: http://127.0.0.1:8000

## How to Contribute to ZimFarm Development

To contribute, please see the CONTRIBUTING document.

## Authors

ZimFarm is a sponsored project of ZimboPy. For a complete list of authors,
please see the AUTHORS file.
