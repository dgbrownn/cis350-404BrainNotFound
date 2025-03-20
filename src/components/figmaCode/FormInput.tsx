"use client";

import * as React from "react";

interface FormInputProps {
  label: string;
  placeholder: string;
  name: string;
}

export const FormInput: React.FC<FormInputProps> = ({
  label,
  placeholder,
  name,
}) => {
  return (
    <div className="mt-14 max-w-full w-[318px] max-md:mt-10">
      <div className="w-full max-w-[318px]">
        <label className="leading-snug text-stone-900" htmlFor={name}>
          {label}
        </label>
        <input
          type="text"
          id={name}
          name={name}
          placeholder={placeholder}
          className="overflow-hidden flex-1 shrink self-stretch px-4 py-3 mt-2 w-full leading-none bg-white rounded-lg border border-solid basis-0 border-zinc-300 min-w-60 text-zinc-400"
        />
      </div>
    </div>
  );
};
