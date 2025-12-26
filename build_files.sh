set -e

echo "🔹 Installing dependencies..."
pip install -r requirements.txt --target .vercel/python

echo "🔹 Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed!"

