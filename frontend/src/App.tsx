import { useEffect, useState } from "react";
import { api } from "./api/client";

export default function App() {
  const [status, setStatus] = useState<"loading" | "ok" | "error">("loading");
  useEffect(() => {
    api.get("/health").then(() => setStatus("ok")).catch(() => setStatus("error"));
  }, []);
  return (
    <main className="min-h-screen grid place-items-center bg-slate-50 text-slate-900">
      <div className="rounded-xl bg-white p-8 shadow">
        <h1 className="text-2xl font-semibold">AI Study Companion</h1>
        <p className="mt-2 text-sm text-slate-600">
          Backend: {status === "loading" ? "checking…" : status === "ok" ? "connected" : "unreachable"}
        </p>
      </div>
    </main>
  );
}
