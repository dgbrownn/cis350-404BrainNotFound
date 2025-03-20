"use client";

import * as React from "react";
import { FormInput } from "./FormInput";
import { Button } from "./Button";

export const AuthenticationForm: React.FC = () => {
  return (
    <section className="ml-5 w-[35%] max-md:ml-0 max-md:w-full">
      <div className="flex flex-col items-center self-stretch my-auto w-full text-base max-md:mt-10 max-md:max-w-full">
        <div className="flex self-stretch w-full text-4xl leading-none whitespace-nowrap text-neutral-100 max-md:max-w-full">
          <Button className="flex-auto gap-2 self-stretch px-3 py-7 text-4xl min-h-[88px]">
            Login
          </Button>
          <img
            src="https://cdn.builder.io/api/v1/image/assets/b17fcf7dd31545898fe7f0a2cf369b68/7d9605b4307deaa2b27c37c16b0c1dfdaa39f66efe0f5d1bb45b7228cc84a804?placeholderIfAbsent=true"
            alt="Decoration"
            className="object-contain shrink-0 my-auto max-w-full aspect-[1.79] w-[141px]"
          />
        </div>

        <img
          src="https://cdn.builder.io/api/v1/image/assets/b17fcf7dd31545898fe7f0a2cf369b68/304552955c8f666772390573f1d1692bfa70521d46afa5f34c78ec87947744c3?placeholderIfAbsent=true"
          alt="Decoration"
          className="object-contain self-stretch mt-24 w-full aspect-[90.91] max-md:mt-10 max-md:max-w-full"
        />

        <h2 className="mt-14 text-6xl text-center text-stone-900 max-md:mt-10 max-md:text-4xl">
          Sign Up
        </h2>

        <form className="w-full flex flex-col items-center">
          <FormInput
            label="First Name"
            placeholder="Ex: John"
            name="firstName"
          />

          <FormInput
            label="Last Name"
            placeholder="Ex: Smith"
            name="lastName"
          />

          <FormInput
            label="Email"
            placeholder="Ex: you@exapmle.com"
            name="email"
          />

          <Button className="px-3 py-4 mt-20 text-2xl max-md:mt-10">
            Sign Up
          </Button>
        </form>
      </div>
    </section>
  );
};
