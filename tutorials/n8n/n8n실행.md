
enroot import -o n8n.sqsh 'docker://n8nio/n8n:latest'

enroot create --name n8n n8n.sqsh

mkdir n8n_data

chmod 600 "$PWD/n8n_data/.n8n/config"

enroot start --rw   -m "$PWD/n8n_data:/data"   --env PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"   --env N8N_HOST=0.0.0.0   --env N8N_PORT=5678   --env N8N_PROTOCOL=http   --env N8N_USER_FOLDER=/data   --env N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true   --env TINI_SUBREAPER=1   n8n