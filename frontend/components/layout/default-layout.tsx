import { Box, Flex } from "@chakra-ui/react";
import { Header } from "../header";

export function DefaultLayout({ children }: { children: React.ReactNode }) {
  return (
    <Flex direction="column">
      <Header />
      <Box
        flex={1}
        margin="auto"
        maxWidth="1200px"
        width="100%"
        padding={4}
        paddingTop={4}
      >
        {children}
      </Box>
    </Flex>
  );
}
