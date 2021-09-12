# Prerequisitos
Copiar service-instance de cos en
```bash
~/.bluemix/cos_credetials
```

# Ejecución en local
```bash
venv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

# Generación de images
```bash
docker login
docker build -t docker.io/jorgehernandezramirez/flask-cos:latest .
docker push docker.io/jorgehernandezramirez/flask-cos:latest
```

# Ejecución en local docker
```bash
docker run -d -p 8080:8080  -v ~/.bluemix:/root/.bluemix docker.io/jorgehernandezramirez/flask-cos:latest
curl localhost:8080/bucket
```

# Ejecución en kubernetes
#### Create cluster free
```bash
ibmcloud ks cluster create classic --name k8s-cluster-free
```

#### Get cluster id
```bash
ibmcloud ks clusters -q | awk '{print $2}'
```

#### Set cluster to kubectl
```bash
ibmcloud ks cluster config -c CLUSTERID
```

#### Service binding
Esto generará un secret con las credenciales de la instancia del servicio. Esta opción no permite crear un fichero cos_credentials con las credenciales que deben ir en ~/.bluemix/cos_credentials. Ir al paso de abajo
```bash
ibmcloud ks cluster service bind --cluster k8s-cluster-free --namespace default --service svc-jorgehernandezramirez
```

otra alternativa es crear a mano el secreto
```
kubectl create secret generic my-secret --from-file=cos_credentials
```

#### Deployment
```
kubectl apply -f k8s-resources.yaml
kubectl proxy --port 8081
curl http://localhost:8081/api/v1/namespaces/default/services/flask-cos-service:http/proxy/bucket
```