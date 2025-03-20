"use client";

import * as React from "react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
  fullWidth?: boolean;
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = "primary",
  fullWidth = false,
  children,
  className = "",
  ...props
}) => {
  const baseStyles =
    "overflow-hidden rounded-lg border border-solid min-h-[60px] text-neutral-100";
  const variantStyles = {
    primary: "bg-zinc-800 border-zinc-800",
    secondary: "bg-transparent border-zinc-300",
  };

  const widthStyles = fullWidth ? "w-full" : "w-80";

  return (
    <button
      className={`${baseStyles} ${variantStyles[variant]} ${widthStyles} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};
