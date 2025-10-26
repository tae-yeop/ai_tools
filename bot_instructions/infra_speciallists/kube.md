쿠버 접근 가능 노드 확인

```yaml
kubectl get nodes
```

노드 상태 및 리소스 확인

```yaml
kubectl describe node aten228
```

쿠버 클러스터에 추가 노드

계산 노드에 커부 구성요소 (kubeadm, kubelet)을 설치

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null
sudo apt-get update
sudo apt-get install -y kubelet kubeadm
sudo apt-mark hold kubelet kubeadm
```

마스터 서버에서 join token 생성 (192.168.1.100:6443 ⇒ 마스터 노드 주소와 쿠버 API 포트)

```bash
kubeadm token create --print-join-command

kubeadm join 192.168.1.100:6443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef

```

계산 서버에서

```bash
sudo kubeadm join 192.168.1.100:6443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef

```

마스터 서버에서 확인

```bash
kubectl get nodes
```

쿠버 pod 실행 삭제

- 작업 내역 yaml 만들기 :  띄어쓰기, 오타 주의

```yaml
apiVersion: v1
kind: Pod
metadata:
	name: test-pod
spec:
	containers:
	- name: test-container
		image: nginx
	nodeName: aten228
```

```python
kubectl apply -f test-pod.yaml
```

- pod 실행 확인

```yaml
kubectl get pods -o wide --field-selector spec.nodeName=aten228
```

- 실행 중지 후 삭제

```yaml
kubectl delete pod test-pod
```

- pod 들어가기

```yaml
kubectl exec -it gpu-pod -- /bin/bash
```