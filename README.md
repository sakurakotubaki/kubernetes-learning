# kubernetes-learning
kubernetesを学ぶためのプロジェクト

🐒猿でもできるKubernetes

[日本語サイト](https://kubernetes.io/ja/#kubernetes-k8s-ja-docs-concepts-overview-%E3%81%AF-%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%82%84%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%92%E8%87%AA%E5%8B%95%E5%8C%96%E3%81%97%E3%81%9F%E3%82%8A-%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E5%8C%96%E3%81%95%E3%82%8C%E3%81%9F%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E7%AE%A1%E7%90%86%E3%81%97%E3%81%9F%E3%82%8A%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AE-%E3%82%AA%E3%83%BC%E3%83%97%E3%83%B3%E3%82%BD%E3%83%BC%E3%82%B9%E3%81%AE%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%A7%E3%81%99)

>Kubernetes (K8s)は、デプロイやスケーリングを自動化したり、コンテナ化されたアプリケーションを管理したりするための、オープンソースのシステムです

## 学習コンテンツ

### 1. [Nginx on Kubernetes](./nginx/nginx.md)
Kubernetesを使用してNginxウェブサーバーを構築、管理する方法を学ぶチュートリアル。以下の内容が含まれています：
- Deploymentマニフェストの作成と管理
- Serviceマニフェストによる公開方法
- ConfigMapを使用したNginx設定のカスタマイズ
- リソースの制限と健全性チェックの設定

すべての実践例とマニフェストファイルは `nginx/manifests/` ディレクトリにあります。

### 学習予定トピック
- [ ] StatefulSet
- [ ] PersistentVolume
- [ ] Ingress
- [ ] Secrets
- [ ] Horizontal Pod Autoscaler

## 更新履歴

- 2025-05-08: Nginxチュートリアル追加