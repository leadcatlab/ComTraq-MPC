# (1) Use a base image that already has conda installed:
FROM continuumio/miniconda3

# (2) Create a working directory inside the container:
WORKDIR /app

# (3) Copy all local files into the container's working directory:
COPY . /app

# (4) Make the setup script executable & run it.
#     The setup.sh script will install conda env and all dependencies.
RUN chmod +x setup.sh
RUN /bin/bash -c "./setup.sh"

# (5) By default, we'll run the test script upon container start.
#     Adjust this as you see fit (e.g., a Jupyter notebook, training script, or a bash shell).
CMD ["python", "src/comtraq-mpc/comtraq-mpc_test.py"]
