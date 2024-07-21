# Images Gallery Backend

## Descripción
Este es el backend del proyecto Images Gallery, desarrollado con Django y Django REST Framework. Proporciona una API para gestionar imágenes y usuarios.

## Estructura del Proyecto

```
imagesgallery_backend/
├── imagesgallery/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── gallery/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## Tecnologías Utilizadas
- Django
- Django REST Framework
- MySQL

## Instalación y Configuración

1. Clona el repositorio:

```bash
git clone https://github.com/rolycore/imagegallery_backend.git
cd imagesgallery/imagesgallery_backend
```

2. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura la base de datos en `imagesgallery/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Realiza las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

7. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

El backend estará disponible en `http://localhost:8000`.

## Estructura de Archivos

```
backend/
├── imagesgallery/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── gallery/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

### Autenticación

- `POST /api/auth/login/`: Iniciar sesión
- `POST /api/auth/register/`: Registrar un nuevo usuario

### Imágenes

- `GET /api/images/`: Listar todas las imágenes
- `POST /api/images/`: Subir una nueva imagen
- `GET /api/images/:id/`: Obtener detalles de una imagen específica
- `PUT /api/images/:id/`: Actualizar una imagen
- `DELETE /api/images/:id/`: Eliminar una imagen

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para cualquier consulta o problema, puedes contactarme a través de [shalomsolutiontech@gmail.com](mailto:shalomsolutiontech@gmail.com).

