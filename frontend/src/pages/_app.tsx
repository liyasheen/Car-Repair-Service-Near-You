import type { AppProps } from "next/app";
import { Providers } from "../../providers";
import { DefaultLayout } from "../../components/layout";

export default function App({ Component, pageProps }: AppProps) {
  console.log(JSON.stringify(pageProps));
  return (
    <Providers>
      <DefaultLayout>
        <Component {...pageProps} />
      </DefaultLayout>
    </Providers>
  );
}
