export default async function handler(req, res) {
  const input = (req.body && req.body.input) || "";
  const hasKey = Boolean(process.env.MIMO_API_KEY);
  const mode = hasKey ? "mimo-ready" : "mock-demo";
  const project = "mimo-devops-assistant";
  const task = "devops";
  const mock = {"diagnosis": ["Disk usage critical on /var", "Application cannot reach PostgreSQL on 127.0.0.1:5432"], "safe_steps": ["Check largest files with du", "Rotate logs", "Verify database service status", "Do not delete data directories blindly"]};
  return res.status(200).json({
    ok: true,
    project,
    task,
    mode,
    input_preview: input.slice(0, 500),
    result: mock,
    next_step: hasKey ? "Connect live MiMo request in this API route." : "Set MIMO_API_KEY in Vercel Environment Variables to enable real MiMo calls."
  });
}
