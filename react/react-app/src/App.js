import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import NavBar from './components/commons/Navbar';
import Users from './components/Users';



function App() {
  return (
    <div className="App">
      <NavBar />
      <div className="container">
        < Users />
      </div>
    </div>
  );
}

export default App;
