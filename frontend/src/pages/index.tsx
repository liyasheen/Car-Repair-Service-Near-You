import { Button } from "@chakra-ui/react";
import Head from "next/head";
import { useHttpClient } from "../../hooks/http-client";
import { useState } from "react";
import WithAction from "../../components/nav-bar/NavBar";
import HomePage from "./homepage";

type Test = {
  services: {
    name: string;
    age: string;
    location: string;
  }[];
};

export default function Home() {
  const [data, setData] = useState<Test | undefined>(undefined);
  const [list, setList] = useState<any>([]);

  const client = useHttpClient();

  const onClick = async () => {
    const result = await client.get("");
    console.log(await result.text());
  };

  const onClick2 = async () => {
    const response = await client.get("about");
    const data = (await response.json()) as Test;
    setData(data);
  };

  const onClick4 = async () => {
    const response = await client.post("filter", {
      json: {
        location: "london",
      },
    });
    const data = (await response.json()) as Test;
    setData(data);
  };

  const onClick3 = async () => {
    const response = await client.post("add", {
      json: {
        name: "Liya" + Date.now(),
        age: "22",
      },
    });

    setList(await response.json());
  };

  return (
    <>
      <main>
        {/* <Button onClick={onClick}>Click</Button> */}
        {/* <Button onClick={onClick2}>Click</Button> */}
        <Button onClick={onClick4}>Click</Button>
        <b> TEXT</b>
        {/* {data && <b>{data.json}</b>} */}
        {JSON.stringify(data)}
        <b>{data?.services[0].location}</b>
      </main>
      {/* <HomePage /> */}
    </>
  );
}
