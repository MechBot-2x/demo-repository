    A[Crear proyecto] --> B[Desarrollo en main]
    B --> C{Preparar deploy}
    C --> |Sí| D[Crear rama gh-pages limpia]
    C --> |No| B
    D --> E[Subir solo archivos deployables]
    E --> F[Configurar GitHub Pages]
