import React from "react";
import Link from 'next/link';
import { signOut } from "supertokens-auth-react/recipe/thirdpartyemailpassword";

export default function NavBar() {
  async function onLogout() {
    await signOut();
    window.location.href = "/";
  }
  return (
    <ul>
      <li><Link href="/auth">
            <button>Login</button>
          </Link></li>
      <li><button onClick={onLogout}>Logout</button></li>
    </ul>
    
  )
}