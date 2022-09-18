import styles from './layout.module.css';
import NavBar from './navbar';

export default function Layout({ children }) {
  return <div className={styles.container}>
    <NavBar />
    {children}
  </div>;
}   