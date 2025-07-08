# 1. Utilise une image légère de Python
FROM python:3.11-slim

# 2. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 3. Copier requirements.txt séparément pour le cache Docker
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# 5. Copier tout le reste du code de l'application
COPY . .

# 6. Collecte les fichiers statiques (optionnel si settings.py est bien configuré)
RUN python manage.py collectstatic --noinput

# 7. Exposer le port que Gunicorn va utiliser
EXPOSE 8000

# 8. Commande de démarrage (production)
CMD
