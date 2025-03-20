import * as React from "react";

export const WelcomeBanner: React.FC = () => {
  return (
    <section className="w-[65%] max-md:ml-0 max-md:w-full">
      <div className="flex relative flex-col grow items-start pt-32 pr-20 pb-72 pl-7 text-black min-h-[1024px] max-md:px-5 max-md:py-24 max-md:mt-10 max-md:max-w-full">
        <img
          src="https://cdn.builder.io/api/v1/image/assets/b17fcf7dd31545898fe7f0a2cf369b68/101510d8501422cbd9f369f478d4dfef277056a8a4836f42555632ed7e6c738c?placeholderIfAbsent=true"
          alt="Background decoration"
          className="object-cover absolute inset-0 size-full"
        />
        <h1 className="relative ml-10 font-medium text-[156px] max-md:max-w-full max-md:text-4xl">
          MacroCal
        </h1>
        <p className="relative mt-96 ml-20 text-7xl text-center max-md:mt-10 max-md:ml-2.5 max-md:text-4xl">
          Welcome
          <br />
        </p>
        <p className="relative mt-24 text-5xl max-md:mt-10 max-md:max-w-full max-md:text-4xl">
          Get Your Health In Check
        </p>
      </div>
    </section>
  );
};
