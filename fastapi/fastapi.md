# FastAPI on Kubernetes - Hello World

このプロジェクトはFastAPIを使用したシンプルなHello World APIをKubernetes上で動かすデモです。
Swagger UI による API ドキュメント自動生成機能も含まれています。

## アプリケーションの構成

- FastAPIを使ったシンプルなREST API
- Swaggerによる自動ドキュメント生成（`/docs`でアクセス可能）
- Kubernetes上での実行環境

## 使用技術

- Python 3.13
- FastAPI
- Docker
- Kubernetes

## 構築手順

以下の手順で環境を構築します。

### 1. Dockerイメージをビルドする

```bash
cd fastapi
docker build -t fastapi-app:latest .
```

### 2. ローカルでの動作確認（オプション）

```bash
docker run -p 8000:8000 fastapi-app:latest
```

ブラウザで http://localhost:8000 にアクセスして動作確認
Swaggerドキュメントは http://localhost:8000/docs で確認できます

### 3. Kubernetesにデプロイ
kubernetes-learningディレクトリで実行する場合のコマンド

```bash
# Deploymentをデプロイ
kubectl apply -f fastapi/manifests/fastapi-deployment.yaml
# startが必要
minikube start
# Serviceをデプロイ
kubectl apply -f fastapi/manifests/fastapi-service.yaml

# Ingressをデプロイ (Ingress Controller必須)
kubectl apply -f fastapi/manifests/fastapi-ingress.yaml
# get pods
kubectl get pods
```

途中動かず対応
```shell
cd fastapi && docker build -t fastapi-app:latest .
kubectl get pods
minikube service fastapi --url
```

アクセスできた!

http://127.0.0.1:51574

### 4. アクセス方法

- API直接アクセス: `http://<your-ingress-ip>/`
- Swagger UI: `http://<your-ingress-ip>/docs`
- ReDoc: `http://<your-ingress-ip>/redoc`

## 環境削除手順

```bash
kubectl delete -f fastapi/manifests/fastapi-ingress.yaml
kubectl delete -f fastapi/manifests/fastapi-service.yaml
kubectl delete -f fastapi/manifests/fastapi-deployment.yaml
```