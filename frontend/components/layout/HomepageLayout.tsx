import { Box, Flex } from "@chakra-ui/react";
import Image from "next/image";
import WithAction from "../nav-bar/NavBar";
import backgroundImage from "../../public/background.jpg";
export function HomepageLayout({ children }: { children: React.ReactNode }) {
  return (
    <Flex direction="column">
      <WithAction />
      {/* <Image src={backgroundImage} alt={""} /> */}
      {children}
    </Flex>
  );
}
