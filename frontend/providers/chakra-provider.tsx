import {
  ChakraProvider as Provider,
  extendTheme,
  Theme,
  withDefaultColorScheme,
} from "@chakra-ui/react";
import { ReactNode } from "react";

const theme = extendTheme(
  withDefaultColorScheme({
    colorScheme: "pink",
  }),
  {
    styles: {
      global: ({ theme }: { theme: Theme }) => ({
        body: {
          bg: theme.colors.gray["100"],
        },
      }),
    },
  }
);

export function ChakraProvider({ children }: { children: ReactNode }) {
  return <Provider theme={theme}>{children}</Provider>;
}
