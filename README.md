## Running the Project with Docker

This project provides a Docker-based setup for the backend service using Python 3.11 and the `uv` dependency manager. The backend is containerized and can be built and run using Docker Compose.

### Requirements
- Docker and Docker Compose installed on your system.
- No external services (e.g., databases) are required by default.

### Build and Run Instructions

1. **Build and start the backend service:**

   ```sh
   docker compose up --build
   ```

   This will build the backend image from `./backend/Dockerfile` and start the service defined in `compose.yaml`.

2. **Accessing the backend:**
   - The backend service will be available at [http://localhost:8000](http://localhost:8000).
   - Port `8000` is exposed and mapped from the container to your host.

### Configuration
- No environment variables are required by default. If you add a `.env` file to `./backend`, uncomment the `env_file` line in `compose.yaml` to enable environment variable support.
- If you add external services (e.g., a database), update `compose.yaml` accordingly and add them to `depends_on` and `networks` as needed.

### Notes
- The backend uses Python 3.11 (slim) and the `uv` dependency manager for efficient dependency management.
- The application is started with Uvicorn, serving FastAPI from `app.main:app`.
