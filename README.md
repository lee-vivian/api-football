# api-football

Got tired of wasting time scrolling through Google results and skimming random websites just to find out when and where my favorite teams were playing so made this app to make it easier to follow specific leagues and clubs #COYG

## Installation Steps
1. Clone the repository. Be sure to clone using SSH so you can push back into the repository using the SSH key stored in your GitHub account settings.

2. Create a virtual env
   ```
   cd /path/to/your/project
   python3 -m venv <myenv>
   ```

3. Activate your virtual env
   ```
   cd /path/to/your/project
   source myenv/bin/activate
   ```
   
   To deactivate your virtual env
   ```
   deactivate
   ```

   To delete your virtual env, delete the virtual env directory
   ```
   cd /path/to/your/project
   rm -r myenv
   ```

5. Install the necessary packages
   ```
   pip install -r requirements.txt
   ```

6. Register on the app-football website https://dashboard.api-football.com/register to get your free API key

7. In env.py, replace API_KEY with your API key value

## Run the app
Run a local python server that will allow you to send requests to the api-football repository and get responses back in JSON-format
   ```
   python3 server.py
   curl localhost:5000/status (or replace localhost with whatever IP address your server is running on)
   ```

## Steps for Developers

### Update python packages required for app
```
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Updated requirements.txt"
git push -u origin main
```

