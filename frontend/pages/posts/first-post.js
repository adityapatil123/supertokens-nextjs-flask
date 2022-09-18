import Head from 'next/head';
import Link from 'next/link';
import Layout from '../../components/layout';
import { ThirdPartyEmailPasswordAuth } from "supertokens-auth-react/recipe/thirdpartyemailpassword";


export default function FirstPost() {
  return (
    <ThirdPartyEmailPasswordAuth>
      <Layout>
        <Head>
          <title>First Post</title>
        </Head>
        <h1>First Post (Protected)</h1>
        <h2>
          <Link href="/">
            <a>Back to home</a>
          </Link>
        </h2>
      </Layout>
    </ThirdPartyEmailPasswordAuth>
  );
}