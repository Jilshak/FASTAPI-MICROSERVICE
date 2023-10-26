import { Routes, Route } from 'react-router-dom'
import LoginPage from './Pages/LoginPage'
import RegisterPage from './Pages/RegisterPage'
import HomePage from './Pages/HomePage'
import ProtectedRoutes from './utils/ProtectedRoutes'

function App() {


  return (
    <Routes>
      <Route path='/login' element={<LoginPage />} />
      <Route path='/register' element={<RegisterPage />} />
      <Route element={<ProtectedRoutes />}>
        <Route index path='/' element={<HomePage />} />
      </Route>
    </Routes>
  )
}

export default App
