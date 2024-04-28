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
          backgroundImage: "background.jpg",
          backgroundSize: "cover",
          backgroundPosition: "0px -50px",
          //   backgroundPosition: "center, center",
          backgroundRepeat: "no-repeat",
          //   width: "100%",
          fontFamily: "Marmelad, sansSerif",
          fontWeight: 400,
          height: "100%",
        },
      }),
      fonts: {
        heading: "Marmelad, sansSerif",
        fontWeight: 400,
      },
    },
  }
);

export function ChakraProvider({ children }: { children: ReactNode }) {
  return <Provider theme={theme}>{children}</Provider>;
}
