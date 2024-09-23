"use client";
import React, { useState } from "react";
import { login } from "@/api/auth";
import { toast } from "react-toastify";
import Loader from "./Loader";

const Login = () => {
  const [usernameOrEmail, setUsernameOrEmail] = useState("");
  const [password, setPassword] = useState("");
  const[loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);

    await new Promise((resolve) => setTimeout(resolve, 1000));

    try {
      const data = await login(usernameOrEmail, password);

      localStorage.setItem("token", data.token);
      console.log("Login bem-sucedido:", data);
      toast.success("Login bem-sucedido!");

      setUsernameOrEmail("");
      setPassword("");

      await new Promise((resolve) => setTimeout(resolve, 1000));
      window.location.href = "/teste";
    } catch (error) {
      console.error("Erro no login:", error);
      const errorMessage = error?.error || "Tente novamente.";
      toast.error("Erro no login: " + errorMessage);

      setUsernameOrEmail("");
      setPassword("");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-[440px] h-[530px] rounded-2xl bg-white">
       {loading && <Loader />}
      <div className="flex flex-col items-center justify-center mt-4">
        <img src="/assets/logotemp2.png" alt="logo 2" className="w-32" />
        <form className="mt-[50px]" onSubmit={handleLogin}>
          <label
            htmlFor="email"
            className="block text-black text-sm font-normal mb-[2px]"
          >
            Email
          </label>
          <input
            type="text"
            id="email"
            className="w-[310px] px-3 py-2 border rounded-[13px] bg-[#e6e6e6] focus:outline-none focus:ring-2 focus:ring-[#8ABF17] text-black"
            value={usernameOrEmail} // Vinculando o valor do input ao estado
            onChange={(e) => setUsernameOrEmail(e.target.value)} // Atualiza o estado ao digitar
          />
          <div className="mt-5">
            <label
              htmlFor="password"
              className="block text-black text-sm font-normal mb-[2px]"
            >
              Senha
            </label>
            <input
              type="password"
              id="password"
              className="w-[310px] px-3 py-2 border rounded-[13px] bg-[#e6e6e6] focus:outline-none focus:ring-2 focus:ring-[#8ABF17] text-black"
              value={password} // Vinculando o valor do input ao estado
              onChange={(e) => setPassword(e.target.value)} // Atualiza o estado ao digitar
            />
          </div>
          <button
            type="submit"
            className="bg-[#6AF41A] p-5 rounded-[13px] uppercase font-bold text-white text-2xl mt-5 w-full"
          >
            Entrar
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
