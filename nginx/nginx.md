# NginxをKubernetesで構築する

## 概要

このチュートリアルでは、Kubernetesを使用してNginxウェブサーバーを構築、実行、管理する方法を学びます。

## 前提条件

- Kubernetesクラスタ（Minikube、Docker Desktop、または他のKubernetesクラスタ）
- kubectl CLIツール
- 基本的なKubernetesの概念の理解

## ステップ1: マニフェストファイルの作成

以下の3つのマニフェストファイルを作成します：

1. `nginx-deployment.yaml` - Nginxのデプロイメント設定
2. `nginx-service.yaml` - Nginxサービスの設定
3. `nginx-configmap.yaml` - Nginxカスタム設定のConfigMap

これらのファイルは `manifests` ディレクトリに保存します。

### ConfigMapの活用

ConfigMapを使用することで、Nginxの設定ファイルをKubernetesマニフェストとして管理できます。このチュートリアルでは、以下の機能を持つカスタムNginx設定を実装します：

- カスタムログフォーマット
- エラーページのカスタマイズ
- ヘルスチェック用エンドポイント（`/health`）

## ステップ1.5: Kubernetesクラスタの起動と設定

### Docker Desktopを使用する場合

1. Docker Desktopを起動し、設定からKubernetesを有効にします：
   - Docker Desktopアイコンを右クリック → 「設定」を開く
   - 「Kubernetes」タブを選択
   - 「Enable Kubernetes」にチェックを入れて「Apply & Restart」をクリック

2. クラスタの状態確認：
```bash
# クラスタの状態確認
kubectl cluster-info

# ノードの状態確認
kubectl get nodes
```

### Minikubeを使用する場合

1. Minikubeを起動：
```bash
# Minikubeを起動
minikube start

# クラスタの状態確認
minikube status
```

### kubectlの設定確認

```bash
# 現在のコンテキスト確認
kubectl config current-context

# 全コンテキスト一覧表示
kubectl config get-contexts
```

### トラブルシューティング

接続エラーが発生した場合は、以下を確認してください：
- Kubernetes クラスタが実行中か
- kubectlが適切なコンテキストを使用しているか
- ~/.kube/config ファイルが正しく設定されているか

ファイアウォール設定などが原因で接続できない場合は、`--validate=false`オプションを使用できます：
```bash
kubectl apply -f manifests/nginx-configmap.yaml --validate=false
```
ただし、バリデーションをスキップするため、マニフェストに問題がある場合でも適用されてしまう点に注意してください。

## ステップ2: デプロイメントの作成と実行

```bash
# まずConfigMapを適用
kubectl apply -f manifests/nginx-configmap.yaml

# 次にデプロイメントとサービスを適用
kubectl apply -f manifests/nginx-deployment.yaml
kubectl apply -f manifests/nginx-service.yaml
```

## ステップ3: デプロイメントの確認

```bash
# Podの状態確認
kubectl get pods

# デプロイメントの確認
kubectl get deployments

# サービスの確認
kubectl get services

# ConfigMapの確認
kubectl get configmaps
```

## ステップ4: Nginxへのアクセス

```bash
# サービスの詳細を表示
kubectl describe service nginx-service

# minikubeを使用している場合
minikube service nginx-service

# ヘルスチェックエンドポイントの確認
curl $(minikube ip):$(kubectl get svc nginx-service -o jsonpath='{.spec.ports[0].nodePort}')/health
```

## ステップ5: リソースの停止と削除

```bash
# サービスの削除
kubectl delete -f manifests/nginx-service.yaml

# デプロイメントの削除
kubectl delete -f manifests/nginx-deployment.yaml

# ConfigMapの削除
kubectl delete -f manifests/nginx-configmap.yaml
```

## Kubernetesリソース解説

### Deployment
Deploymentは、アプリケーションのデプロイに関する情報を記述するリソースです。レプリカ数、コンテナイメージ、リソース制限などを設定します。

### Service
Serviceは、Podへのネットワークアクセスを提供するリソースです。このチュートリアルでは、NodePortタイプのServiceを使用して、クラスタ外部からNginxにアクセスできるようにしています。

### ConfigMap
ConfigMapは、設定情報をキーと値のペアとして保存するリソースです。このチュートリアルでは、Nginxの設定ファイルをConfigMapとして管理しています。

## 参考資料

- [Kubernetes公式ドキュメント](https://kubernetes.io/docs/home/)
- [Nginx公式ドキュメント](https://nginx.org/en/docs/)

## 更新履歴

- 2025-05-08: 初回作成