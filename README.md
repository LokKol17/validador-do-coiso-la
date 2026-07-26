# validador

Validador de senhas via API HTTP.

## Endpoints

- `GET /` — redireciona para instruções
- `GET /brew_coffee` — easter egg (HTTP 418)
- `POST /validate` — valida uma senha

### POST /validate

```json
{ "password": "minhaSenha123" }
```

Regras validadas:
- mínimo 8 caracteres
- sem espaços
- pelo menos 1 letra maiúscula
- pelo menos 1 letra minúscula
- pelo menos 1 número

## Como rodar

```bash
docker build -t validador .
docker run -p 5000:5000 validador
```
