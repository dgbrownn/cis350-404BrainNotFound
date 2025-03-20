"use client";

import * as React from "react";
import { WelcomeBanner } from "./WelcomeBanner";
import { AuthenticationForm } from "./AuthenticationForm";

export const SignInLoginScreen: React.FC = () => {
  return (
    <main className="overflow-hidden pr-20 bg-blue-100 max-md:pr-5">
      <div className="flex gap-5 max-md:flex-col">
        <WelcomeBanner />
        <AuthenticationForm />
      </div>
    </main>
  );
};

export default SignInLoginScreen;
