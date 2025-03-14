# Survey Data Visualization Dashboard

Interactive dashboard for visualizing survey data built with Dash.

## Deployment on Render

1. Create a new Git repository with all the files from this folder
2. Sign up for a [Render](https://render.com/) account if you don't have one
3. In the Render dashboard, click "New +" and select "Web Service"
4. Connect your repository
5. Configure your web service with these settings:
   - Name: survey-dashboard (or your preferred name)
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:server`
6. Click "Create Web Service"

Your dashboard will be available at the URL provided by Render once the deployment is complete!
