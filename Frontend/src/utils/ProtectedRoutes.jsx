import { Navigate, Outlet } from 'react-router-dom'
import React, { useEffect } from 'react'
import jwtDecode from 'jwt-decode'

function ProtectedRoutes() {
    let authentication = localStorage.getItem('fastauth')

    return (
        authentication && jwtDecode(authentication)?.sub != null && jwtDecode(authentication)?.id != null ? <Outlet /> : <Navigate to='/login' />
    )
}

export default ProtectedRoutes