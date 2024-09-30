# Stop the script if any command fails
set -o errexit

# Install the required packages from the requirements.txt file
pip install -r requirements.txt

# Collect static files (this will move them to the static directory defined in your settings)
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
