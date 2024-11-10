#! /bin/bash
## replace DASHBOARD_URL with the hostname you want for your dashboard
## the hostname should be setup to point to your ingress controller

DASHBOARD_URL=localhost.nip.io ## change me to your localhost IP !
kubectl apply -n tekton-pipelines -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tekton-dashboard
  namespace: tekton-pipelines
spec:
  rules:
  - host: $DASHBOARD_URL
    http:
      paths:
      - pathType: ImplementationSpecific
        backend:
          service:
            name: tekton-dashboard
            port:
              number: 9097
EOF

