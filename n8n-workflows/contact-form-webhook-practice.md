# Contact Form Webhook Practice

## Goal
Learn how webhooks and workflow logic work in n8n.

---

## Workflow Architecture

Webhook Trigger
↓
IF Node (Check message content)
↓
TRUE → Respond: "Message received successfully"
FALSE → Respond: "Invalid message"

---

## Concepts Practiced

- Webhook Trigger
- POST Requests
- JSON Body
- IF Conditions
- TRUE/FALSE Branches
- Respond to Webhook Node

---

## Example JSON Request

```json
{
  "name": "Reem",
  "email": "reem@test.com",
  "message": "Hello"
}
```

---

## PowerShell Test Command

```powershell
Invoke-RestMethod -Uri "http://localhost:5678/webhook-test/contact-form" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"name":"Reem","email":"reem@test.com","message":"Hello"}'
```

---

## What I Learned

- How automation workflows receive data
- How conditions split workflow paths
- How webhooks connect applications
- Basic API request structure